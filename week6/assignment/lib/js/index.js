$('.box_tools').not('.box_tile').click(function () {
    $(this).toggleClass('box_border_blue');
});


$('.box_tools').not('.box_tile').hover(function () {
    $(this).toggleClass('box_border_red');
});

$("body").click(function (event) { //get id of item clicked 
    console.log("clicked: " + event.target.id);
});
