url="https://api.twitter.com/2/tweets/search/recent?query=from:brennandunn&tweet.fields=created_at,public_metrics"

BEARER_TOKEN=""

curl --request GET $url --header "Authorization: Bearer $BEARER_TOKEN"
