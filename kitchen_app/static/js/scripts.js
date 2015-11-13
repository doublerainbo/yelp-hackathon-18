var feedMe = function () {
    "use strict";
    var $ = this.$, document = this.document, console = this.console;
    $(document).ready(function () {
        console.log("test");

        $('.header-extension').hide();
        
        $('.new-order').click(function () {
            $('.header-extension').slideToggle(300);
        });
        
        $('.order-submit').click(function () {
            $('.header-extension').slideToggle(300);
        });
        
        $(".grid-toggle").click(function () {
            $('.order-container').toggleClass('grid');
            $('.header').slideToggle(300);
            $('.new-order').slideToggle(300);
            $('.floor').toggleClass('kitchen-view');
            
            if ($('.header-extension').is(':visible')) {
                $('.header-extension').slideToggle(300);
            }
        });
    });
};

feedMe.call(this);