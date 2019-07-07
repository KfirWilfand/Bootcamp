$(document).ready(function () {
    getImages(); 
});
getImages = function() {
  $.ajax({
    type: "GET",
    url: "http://itc-colors.appspot.com/get_images",
    dataType: "json",
    success: function (ingArr) {
        displayImages(ingArr); 
    },
    error: function(msg) {
      console.log("error");
    }
  });
};

displayImages = function(ingArr) {
    ingArr.forEach(imageUrl => {
        $('body').append(`<img src='${imageUrl}'></img>`);   
    });
};
