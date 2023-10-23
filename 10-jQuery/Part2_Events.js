// Clicking specific functions
$('h1').click(function(){
    console.log('There was a click!')
    $(this).text("I was changed!")
})

$('li').click(function(){
    console.log('any li was clicked!')
})

// Key press
$('input').eq(0).keypress(function(event){
    if (event.which === 13){
        $('h3').toggleClass('turnBlue')
    }
})

// on()
$('h1').on('mouseenter', function(){
    $(this).toggleClass('turnBlue')
})

$('input').eq(1).on('click',function(){
    $('.container').slideUp(3000)
})