import os, sys

ret = os.fork()
print("Return Value: ", ret)
# retとは何か？ -> 子プロセスのPIDが返される

if ret == 0:
    print("Child Process: ", os.getpid())
    print("Parent Process: ", os.getppid())
    os.execve("/bin/echo", ["echo", "Hello, World!(pid={})".format(os.getpid())], {})
    exit()
elif ret > 0:
    print("Parent Process: ", os.getpid())
    print("Child Process: ", ret)
    sys.exit()

sys.exit(1)