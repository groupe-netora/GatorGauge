"""Execute analysis for commits."""

from emoji_library import get_emojis_count
from analyze_sentiment import get_avg_sentiment
import parse_commits
import gg_gensim
from analyze_comments import embed_stats_into_html


def analyze_commits(out):
    """Execute analysis for commits."""

    list_of_commits = parse_commits.get_list_of_commits(out)

    write_string = ""
    print("Number of commits: " + len(list_of_commits))
    write_string += "Number of commits: " + len(list_of_commits)

    gg_gensim.gensim_analysis(list_of_commits)

    sentiment = get_avg_sentiment(list_of_commits)
    for key, value in sentiment.iteritems():
        print(key, value)
        write_string += key + ", " + value + "\n"

    emojis_count = get_emojis_count(list_of_commits)
    for key, value in emojis_count.iteritems():
        print(key, value)
        write_string += key + ", " + value + "\n"

    embed_stats_into_html(write_string)