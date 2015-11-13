var feedMe = function () {
    "use strict";
    var $ = this.$, document = this.document, console = this.console;
    $(document).ready(function () {
        console.log("test");

        $('.header-extension').hide();
        
        $('.new-order').click(function () {
            $('.new-order').toggleClass('rotate');
            $('.header-extension').slideToggle(300);
        });
        
        $('.order-submit').click(function () {
            $('.header-extension').slideToggle(300);
        });
        
        $(".choose-floor-button").click(function () {
            $('.choose-floor').slideToggle(300);
            if ($(".choose-floor-button").text() === "Choose floor") {
                $(".choose-floor-button").text("Close");
            } else {
                $(".choose-floor-button").text("Choose floor");
            }
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
        
        $(".requests-floor").change(function () {
            var floor = $(this).find("option:selected").text();
            
            console.log(floor);
            
            self.post("http://127.0.0.1:8000/api/kitchen_requests", { floor: floor })
                .done(function (data) {
                    console.log("Data Loaded: " + data);
                
                    var jsonData = JSON.parse(data);
                    
                    self('.all-orders').html('');

                    self.each(jsonData, function (i, item) {
                        
                        $('.all-orders').append('<div class="order-container"><div class="order-details"><div class="what">' +
                                                item.item + '</div><div class="who">'
                                                + item.requester + ' - located at: '
                                                + item.employee_location + '</div></div>'
                                                + '<img class="complete-icon" src="static/images/check.png"></div>');
                        
                    });
                    
                    
                });
                  
        });
        
    });
};

feedMe.call(this);