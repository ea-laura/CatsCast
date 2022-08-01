from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import sys
import argparse

def main(textfile, stopfile, maskfile, interactive, outfile):
    text = open(textfile, 'r').read()\
        .replace('\u2019', "'")
    stopwords = set(STOPWORDS)
    if stopfile is not None:
        for word in open(stopfile, 'r').read().split():
            stopwords.add(word)
    mask = np.array(Image.open(maskfile)) if maskfile else None
    wc = WordCloud(stopwords=stopwords, mask=mask,
                   background_color='black', contour_color='white',
                   contour_width=2.0, colormap='Spectral')
    wordcloud = wc.generate(text)
    if outfile:
        wc.to_file(outfile)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    if interactive:
        plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--stop", help="file with stopwords")
    parser.add_argument("-m", "--mask", help="image file for mask")
    parser.add_argument("-i", "--interactive", action="store_true",
                        default=False,
                        help = "display wordcloud interactively")
    parser.add_argument("-o", "--outfile", help = "write png to outfile")
    parser.add_argument("textfile")
    args = parser.parse_args()
    main(args.textfile, args.stop, args.mask, args.interactive, args.outfile)
    
