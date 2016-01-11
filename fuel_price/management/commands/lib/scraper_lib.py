import urllib
import urllib2
from progressbar import Percentage, Bar, RotatingMarker, ProgressBar, ETA, FileTransferSpeed
def download_url(url, save_location):
    widgets = ['Test: ', Percentage(), ' ', Bar(marker=RotatingMarker()), ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets)
    def dlProgress(count, blockSize, totalSize):
        if pbar.maxval is None:
            pbar.maxval = totalSize
            pbar.start()
        pbar.update(min(count*blockSize, totalSize))
    urllib.urlretrieve(url, save_location, reporthook=dlProgress)
    pbar.finish()

    # using urllib2
    # f = urllib2.urlopen(url)
    # data = f.read()
    # with open(save_location, "wb") as f:
    #     f.write(data)

    # HTTP request
    # r = requests.get(url)
    # with open(save_location, "wb") as f:
    #     f.write(r.content)
