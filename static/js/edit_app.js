$(function () {


    /* Collapse */
    $("[data-collapse]").on("click", function (event) {
        event.preventDefault();

        var $this = $(this),
            blockId = $this.data('collapse');

        $this.toggleClass("active");
        $("#btn_name").addClass("active");
    });

    /* Collapse */
    $("[data-cop]").on("click", function (event) {
        event.preventDefault();

        var $this = $(this),
            blockId = $this.data('cop');

        $this.toggleClass("active");
        $("#service_off").toggleClass("active");
        $("#service_on").toggleClass("active");
    });

    var holidays = [
        [14,10,2022],
        [15,10,2022]
    ];

    /*$(function () {
        $("#datepicker").datepicker({
            beforeShowDay: function (date) {
                for (var i = 0; i < holidays.length; i++) {
                    if (holidays[i][0] == date.getDate() && holidays[i][1] - 1 == date.getMonth()&& holidays[i][2] == date.getFullYear()) {
                        return [false];
                    }
                }
                return [true];
            }
        });
    });*/
    /*$(function () {
        $("#datepicker").datepicker({
            minDate: 0,
            beforeShowDay: function(date){
			var dayOfWeek = date.getDay();
			if (dayOfWeek == 0 || dayOfWeek == 6){
				return [false];
			} else {
				return [true];
			}
		}
        });
    });*/

});