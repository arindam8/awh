tweets = JSON.parse(tweets)
for (let i = 0; i < tweets.length; i++) {
   tweets[i].text = tweets[i].text.split("http")[0]
   tweets[i].created = tweets[i].created.split(" ")[0]
   tweets[i].created = new Date(tweets[i].created)
   tweets[i].created = tweets[i].created.toLocaleDateString();
   tweets[i].created = tweets[i].created.replace(/\//g, '.');
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.news_date').forEach((date, i) => {date.innerHTML = tweets[i].created})
    document.querySelectorAll('.news_date').forEach((date, i) => {date.setAttribute('href', tweets[i].link_)})
    document.querySelectorAll('.news_content').forEach((content, i) => {content.innerHTML = tweets[i].text})
    document.querySelectorAll('.news_link').forEach((link, i) => {link.setAttribute('href', tweets[i].link_)})
})