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
        
        var self = $;
        $(".order-floor").change(function () {
            var floor = $(this).find("option:selected").text();
            
            console.log(floor);
            
            self.post("http://127.0.0.1:8000/api/available_items", { floor: floor })
                .done(function (data) {
                    console.log("Data Loaded: " + data);
                
                    var jsonData = JSON.parse(data);
                    
                    self('.order-item').html('');

                    self.each(jsonData, function (i, item) {
                        $('.order-item').append($('<option>', {
                            value: item.id,
                            text : item.name
                        }));
                    });
                });
                  
        });
    });
};

feedMe.call(this);