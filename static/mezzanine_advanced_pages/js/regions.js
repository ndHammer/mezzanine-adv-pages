
$(function() {
	$('a[href=#addblock]').on('click', function(e) {
		e.preventDefault()
		var reg = $(e.currentTarget).data('region');
		$('#pageRegion').val(reg);
		$('#blockModal').modal('show');
	});
});