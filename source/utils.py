import speedtest

def measure():
    s = speedtest.Speedtest()
    s.upload(pre_allocate=False)
    #s.get_servers(servers)
    s.get_best_server()
    s.download(threads=1)
    s.results.share()

    results_dict = s.results.dict()
    return results_dict

if __name__ == "__main__":
    print(measure())