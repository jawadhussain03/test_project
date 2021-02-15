import subprocess
import shlex


class Cutils:
    def __init__(self, cmd):
        self.cmd = cmd

    def output(self):
        p1 = subprocess.Popen(shlex.split(self.cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        out, err = p1.communicate()
        if out:
            return (out)
        else:
            return (err)


if __name__ == '__main__':
    x = Cutils('ls')
    print(x.output())
    y = Cutils('ls -lrt')
    print(y.output())