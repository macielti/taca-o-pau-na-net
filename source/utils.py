import speedtest
import os, shutil


def measure():
    s = speedtest.Speedtest()
    s.upload(pre_allocate=False)
    # s.get_servers(servers)
    s.get_best_server()
    s.download(threads=10)
    s.results.share()

    results_dict = s.results.dict()
    return results_dict


def clear_instabot_files(username):
    files = ("blacklist.txt", "comments.txt", "followed.txt",
             "friends.txt", "skipped.txt", "unfollowed.txt", "whitelist.txt", "{}_uuid_and_cookie.json".format(username))
    # remove files
    for filename in files: 
        os.remove(filename) 

    dirs = ("log", "config")
    # remove dirs
    for dir in dirs:
        shutil.rmtree(dir)


if __name__ == "__main__":
    print(measure())
