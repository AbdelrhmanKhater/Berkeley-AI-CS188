import os
import argparse

PROJECT = {
    0: "project0-tutorial",
    1: "project1-search",
    2: "project2-multiagent",
    3: "project3-reinforcement"
}


def check_project(string):
    try:
        project = int(string)
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid project (must be an integer)")
    if 0 <= project <= 3:
        return project
    raise argparse.ArgumentTypeError("Invalid project (must be in [0..3] range)")


def run_project(i):
    print
    print '**********************************************************************'
    print '****************************** Project {} *****************************'.format(i)
    print '**********************************************************************'
    print
    os.system("sleep 2 && cd " + PROJECT[i] + "&& python autograder.py")


def main():
    parser = argparse.ArgumentParser(description='Run Berkeley AI CS188 projects')
    parser.add_argument('-p', '--project',
                        help='project to run (all by default)',
                        type=check_project)
    args = parser.parse_args()

    if args.project is None:
        map(run_project, PROJECT)
    else:
        run_project(args.project)

if __name__ == '__main__':
    main()
