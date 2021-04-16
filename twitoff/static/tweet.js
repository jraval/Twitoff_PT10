// document.getElementById('tweet_text_input').value = "please enter your tweet text";
// document.getElementById('tweet_submit').onclick = function(){
//    document.getElementById('tweet_text_input').value = "this doesn't do anything now, but next lecture we will save your tweet to the database.";
// };
// Update tweet.js with the changes John made, 1) - Button and in user route 2) Similar box and buttton for the tweet
// Open up inspect to make sure it's not cached in browser, make sure you hit refresh so JS is refreshed.
$('#author_submit').click(function() {
    $.ajax({
        url: '/user?twitter_handle=' + $('#author_name_input').val(),
        type: 'GET',
    });
});
$('#tweet_submit').click(function() {
    $.ajax({
        url: '/predict_author?tweet_to_classify=' + $('#tweet_text_input').val(),
        type: 'GET',
        success: function (response){
            $('#classify_response').html(response)
        }
    });
});

