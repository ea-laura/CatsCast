To create a new episode wordcloud:
1. Save the episode as utf-8 text. If it's a Word file, make sure no formatting is showing, then save as text and select utf-8 for encoding and CR+LF for line separators.
2. Remove any extranneous header info from the text file.
3. Run wcloud: python wcloud.py -m cat.jpg -o <episode_dir>/wordcloud.jpg <episode_dir>/<text_file>
4. If you want, you can also include words in a stop file and specify that with the -s flag
5. Edit the wordcloud file to remove everything but the wordcloud.
