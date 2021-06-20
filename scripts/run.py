# Shachar Markovich
# Naor Maman

import argparse
import os

try:
    import progressbar
except:
    print("[!] Error! progressbar package is not install!")
    print("[!] Please install it first, by:\n\tpip install progressbar")


def parse():
    """
    parse the line args.

    :return: the line args
    """
    parser = argparse.ArgumentParser(description='AutoDebugDocker.')
    parser.add_argument('path', metavar='path', type=str, help='path to file')
    # example for tools: radare2 gcc gdb
    parser.add_argument('tools', metavar='tools', type=str, help='list of analysis tools name')
    parser.add_argument('name', metavar='name', type=str, help='docker analysis name')
    args = parser.parse_args()

    if not os.path.isfile(args.path):
        print("File not Found")
        return

    return args


def install_qemu():
    """
    Install qemu utility.
    """
    print("installing qemu")
    os.system("sudo apt-get install qemu binfmt-support qemu-user-static")
    print("installing qemu complete")


def get_dependencies(path: str) -> list:
    """
    get the dependencies files' name of the given file path
    :param path: the path to the suspicious file
    :return: list of dependencies files' name
    """
    output = os.popen(f"readelf -d {path} | grep 'NEEDED'").read()
    # extract the dependencies files' name
    dependencies = []
    for line in output.splitlines():
        dependencies.append(line.split('[')[1].split(']')[0])

    return dependencies


def get_machine_arch(path: str) -> str:
    """
    get the appropriate machine architecture of the suspicious file
    :param path: the path to the suspicious file
    :return: machine architecture
    """
    find_file_arch_command = f"readelf -h {path} | grep 'Class\|Machine'"
    process = os.popen(find_file_arch_command)
    output = process.read()
    bits = output.splitlines()[0].split(' ')[-1][-2:]
    machine = output.splitlines()[1].split(' ')[-1]
    arch = ""
    if bits == '64':
        if machine == 'X86-64':
            arch = 'amd64'
        elif machine == 'ARM':
            arch = 'arm64v8'
        else:
            print(f"Not supported\nbits:\t{bits}\nmachine:\t{machine}")
            exit()

    elif bits == '32':
        if machine == 'ARM':
            arch = 'arm32v7'
        elif machine == '80386':
            arch = 'i386'
        else:
            print(f"Not supported\nbits:\t{bits}\nmachine:\t{machine}")
            exit()
    else:
        print(f"Unexpected behavior\nbits:\t{bits}\nmachine:\t{machine}")
        exit()

    return arch + '/'


def main():
    args = parse()
    dependencies = get_dependencies(args.path)
    arch = get_machine_arch(args.path)

    os.system("sudo apt-file update")
    print("[!] apt-file update complete")

    print("[!] Searching Dependencies")

    bar = progressbar.ProgressBar(maxval=len(dependencies),
                                  widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()

    packages_to_install = set()
    for i, dependency in enumerate(dependencies):
        process_output = os.popen(f"sudo apt-file search {dependency}").read()
        output = process_output.splitlines()[0].split(':')[0]  # get the first dependency, it the most suitable
        packages_to_install.add(output)
        bar.update(i)

    bar.finish()

    dockerfile = f"""FROM {arch}ubuntu
COPY {args.path} $HOME
RUN apt-get update && apt-get install -y {args.tools} {" ".join(packages_to_install)}
RUN groupadd -g 2000 testgroup && useradd --no-log-init -m -u 2001 -g testgroup testuser
USER testuser"""

    with open("dockerfile", "w+") as f:
        f.write(dockerfile)

    print("[!] setting up docker for qemu:")
    os.system("sudo docker run --rm --privileged multiarch/qemu-user-static --reset -p yes")
    print("[!] building docker image")
    os.system("sudo docker build -t malware_analysis .")
    print("[!] building docker image complete")

    print("\n\n[!] Process Complete!\n\n")
    os.system("sudo service docker start")
    os.system(f"sudo docker run -dit --memory=256m --name {args.name} malware_analysis")
    os.system(f"sudo docker attach {args.name}")


if __name__ == '__main__':
    main()
