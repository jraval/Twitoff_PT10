document.getElementById('tweet_text_input').value = "please enter your tweet text";
document.getElementById('tweet_submit').onclick = function(){
    document.getElementById('tweet_text_input').value = "this doesn't do anything now, but next lecture we will save your tweet to the database.";
};
// Update tweet.js with the changes John made, 1) - Button and in user route 2) Similar box and buttton for the tweet
// Open up inspect to make sure it's not cached in browser, make sure you hit refresh so JS is refreshed.