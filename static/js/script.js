/*global console, $, alert*/
/*
  reizing the height of the iframe according to the contentDocument
*/
function resizeIframe(){
  'use strict';
  var iFrame = document.getElementById('myframe'),
      cont = iFrame.contentDocument,
      contHeight = cont.body.offsetHeight;
  iFrame.height = contHeight;
  setInterval(function(){
	'use strict';
    var iFrame = document.getElementById('myframe'),
        cont = iFrame.contentDocument,
        contHeight = cont.body.offsetHeight;
    iFrame.height = contHeight;
  }, 1000);
};
$(function () {
  'use strict';
  /*
    set the height of the background of header = the height of the window
    '.header' => for all the headers of the website except the home page
    '.home-header' => just the header of the home page only
  */
  $('.header').height($(window).height() - 225);
  $('.home-header').height($(window).height());
  /*
    centering the div('.head-title') vertical and horizontal
  */
  $('.header .head-title').css({
    marginTop: (($('.header').height() - $('.header .head-title').height()) / 2.5)
  });
  $('.header .head-title').css({
    marginLeft: (($('.header').width() - $('.header .head-title').width()) / 2)
  });
  /*
    set the height of the background of header = the height of the window in resize() function
    '.header' => for all the headers of the website except the home page
    '.home-header' => just the header of the home page only
  */
  $(window).resize(function () {
    $('.header').height($(window).height() - 200);
    $('.home-header').height($(window).height());
    $('.header .head-title').css({
      marginTop: (($('.header').height() - $('.header .head-title').height()) / 2.5)
    });
    $('.header .head-title').css({
      marginLeft: (($('.header').width() - $('.header .head-title').width()) / 2)
    });
  });
  /*
    changing the type of the input field from date to text when focuesd
    and reverse it when blured
  */
  $('.departure').focus(function () {
    $(this).attr('type', 'date');
  });
  $('.departure').blur(function () {
    $(this).attr('type', 'text');
  });
  /*
    switching follow button color with click in log in form
  */
  $('.switchbtns input').on('click', function () {
    $(this).siblings().removeClass('active');
    $(this).addClass('active');
    $('#log').attr('value', $(this).attr('value'));
  });
  /*
    switching follow button color with click in home page
  */
  $('.vote-info button').on('click', function() {
    if($(this).hasClass('voted')){
      $(this).toggleClass('voted');
    }else{
      $(this).siblings().removeClass('voted');
      $(this).addClass('voted');
    }
  });
  /*
    resizing the height of the image of the vote
  */
  $('.main-vote .vote-img').height($('.main-vote').height());
  $(window).resize(function () {
    $('.main-vote .vote-img').height($('.main-vote').height());
  });
  /*
    switching follow button color with click in home page
  */
  if ($('.agency-card button').hasClass('followed')) {
    $(this).text('unfollow');
  } else if ($('.agency-card button').hasClass('')) {
    $(this).text('follow');
  }
  $('.agency-card button').on('click', function () {
    $(this).toggleClass('followed');
    if ($(this).hasClass('followed')) {
      $(this).text('unfollow');
    } else if ($(this).hasClass('')) {
      $(this).text('follow');
    }
  });
  /* this one for the button in the user-agency page */
  if ($('.tabs-panel .prof-intro button').hasClass('followed')) {
    $(this).text('unfollow');
  } else if ($('.tabs-panel .prof-intro button').hasClass('')) {
    $(this).text('follow');
  }
  $('.tabs-panel .prof-intro button').on('click', function () {
    $(this).toggleClass('followed');
    if ($(this).hasClass('followed')) {
      $(this).text('unfollow');
    } else if ($(this).hasClass('')) {
      $(this).text('follow');
    }
  });
  /*
    sliding down the filter in trips
  */
  $('.filter h2').on('click', function () {
    $('.filter form').slideToggle(800);
  });
  /*
    linking each tab with it's page in profile page
  */
  $('.prof-tabs button').on('click', function () {
    $(this).siblings().removeClass('active');
    $(this).addClass('active');
    $('#' + $(this).data('id')).siblings().fadeOut(500).removeClass('active');
    $('#' + $(this).data('id')).fadeIn(500).addClass('active');
  });
  /*
    linking each tab(history, saved) with it's page in my trips page
  */
  $('.my-trips-tabs form').on('click', function () {
    $(this).siblings().removeClass('active');
    $(this).addClass('active');
    $('#' + $(this).data('id')).siblings().fadeOut(500).removeClass('active');
    $('#' + $(this).data('id')).fadeIn(500).addClass('active');
  });
  /*
    linking each tab(description, reviews) with it's page in trip page
  */
  $('.trip-tabs div').on('click', function () {
    $(this).siblings().removeClass('active');
    $(this).addClass('active');
    $('#' + $(this).data('id')).siblings().fadeOut(500).removeClass('active');
    $('#' + $(this).data('id')).fadeIn(500).addClass('active');
  });
  /*
    removing comment with the click of an icon
  */
  $('.comment-box i').on('click', function () {
    $(this).parent().slideUp(2000, function(){
      $(this).remove();
    });
  });
  /*
    Scroll To Top Button
  */
  $(window).on('scroll', function () {
    if ($(window).scrollTop() > 500) {
      $('.scroll-top').fadeIn(250);
    } else {
      $('.scroll-top').fadeOut(250);
    }
  });

  $('.scroll-top').click(function () {
    $('html, body').animate({
      scrollTop: 0
    }, 1000);
  });

  $('.scroll-top').hover(function () {
    $('.scroll-top span').animate({
      left: '8px',
      opacity: 1
    }, 250);
  }, function () {
    $('.scroll-top span').animate({
      left: '50%',
      opacity: 0
    }, 250);
  });
  /*
    the trigger of skitter (slider)
  */
  $('.skitter-large').skitter({
    interval: 3000,
    navigation: true,
    label: false,
    numbers: true,
    numbers_align: "right",
    dots: false,
    preview: true,
    thumbs: false,
    focus: true,
    controls: true
  });
});
