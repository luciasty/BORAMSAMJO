"use strict";


// main
const tabber = document.querySelector(".tabber");

tabber.addEventListener("click", (e) => {
  if (e.target.classList.contains("tab-trigger")) {
    e.preventDefault();
    const tab = e.target;
    const panels = e.target.parentElement.parentElement.parentElement.querySelectorAll(
      ".tab-panel"
    );
    Array.from(tab.parentElement.parentElement.children)
      .filter((tabF) => tab !== tabF)
      .forEach((tab) => tab.classList.remove("active"));
    tab.parentElement.classList.add("active");
    panels.forEach((panel) =>
      tab.href.split("#").pop() === panel.getAttribute("content-id")
        ? panel.classList.add("active")
        : panel.classList.remove("active")
    );
  }
});

//bar
$(document).ready(function() {
  $('#progressbar').progress_fnc();
  $('.progressStart').on('click', function() {
    var perent = $(this).closest("div").attr("id");
    $('#' + perent).progress_fnc({ type: 'start' });
  });
  $('.progressReset').on('click', function() {
    var perent = $(this).closest("div").attr("id");
    $('#' + perent).progress_fnc({ type: 'reset' });
  });
});
(function($) {
  $.fn.progress_fnc = function(options) {
    var settings = $.extend({
      type: 'start'
    }, options);
    var div = $(this);
    var progress = div.find('.cssProgress');
    progress.each(function() {
      var self = $(this);
      var progress_bar = self.find('.cssProgress-bar');
      var progress_label = self.find('.cssProgress-label, .cssProgress-label2');
      var progress_value = progress_bar.data('percent');
      var percentage = parseInt(progress_value, 10) + '%';
      progress_bar.css({'width': '0%', 'transition': 'none', '-webkit-transition': 'none', '-moz-transition': 'none'});
      if(settings.type == 'start') {
        progress_bar.animate({
          width: percentage
        }, {
          duration: 1000,
          step: function(x) {
            progress_label.text(Math.round(x) + '%');
          }
        });
      } else if(settings.type == 'reset') {
        progress_bar.css('width', '0%');
        progress_label.text('0%');
      }
    });
  }
}(jQuery));

//월간

$(document).ready(function() {
  $('#progressbar2').progress_fnc();
  $('.progressStart').on('click', function() {
    var perent = $(this).closest("div").attr("id");
    $('#' + perent).progress_fnc({ type: 'start' });
  });
  $('.progressReset').on('click', function() {
    var perent = $(this).closest("div").attr("id");
    $('#' + perent).progress_fnc({ type: 'reset' });
  });
});
(function($) {
  $.fn.progress_fnc = function(options) {
    var settings = $.extend({
      type: 'start'
    }, options);
    var div = $(this);
    var progress = div.find('.cssProgress');
    progress.each(function() {
      var self = $(this);
      var progress_bar = self.find('.cssProgress-bar');
      var progress_label = self.find('.cssProgress-label, .cssProgress-label2');
      var progress_value = progress_bar.data('percent');
      var percentage = parseInt(progress_value, 10) + '%';
      progress_bar.css({'width': '0%', 'transition': 'none', '-webkit-transition': 'none', '-moz-transition': 'none'});
      if(settings.type == 'start') {
        progress_bar.animate({
          width: percentage
        }, {
          duration: 1000,
          step: function(x) {
            progress_label.text(Math.round(x) + '%');
          }
        });
      } else if(settings.type == 'reset') {
        progress_bar.css('width', '0%');
        progress_label.text('0%');
      }
    });
  }
}(jQuery));

