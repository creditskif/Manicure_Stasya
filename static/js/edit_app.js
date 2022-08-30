$(function() {
    
    
 /* Collapse */
    $("[data-collapse]").on("click", function(event) {
        event.preventDefault();

        var $this = $(this),
            blockId = $this.data('collapse');

        $this.toggleClass("active");
        $("#btn_name").addClass("active");
    });
    
    /* Collapse */
    $("[data-cop]").on("click", function(event) {
        event.preventDefault();

        var $this = $(this),
            blockId = $this.data('cop');

        $this.toggleClass("active");
        $("#service_off").toggleClass("active");
        $("#service_on").toggleClass("active");
    });
    
});