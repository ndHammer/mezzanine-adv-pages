
$(function() {
	
	$('.region-actions').hide();
	$('.region-block-actions').hide();
	$('.block-region').css('min-height', '50px').css('border', '1px solid transparent').css('min-width', '100px');
	
	$('a[href=#addblock]').on('click', function(e) {
		e.preventDefault()
		var reg = $(e.currentTarget).data('region');
		$('#pageRegion').val(reg);
		$('#blockModal').modal('show');
	});
	
	$('.block-delete').on('submit', function() {
		if(confirm('Are you sure you want to delete this block')) {
			return true;
		};
		return false;
	});
	
	$('.block-region').hover(function(e) {
		$(this).find('.region-actions').show('fast');
		$(this).css('border', '1px solid #000').css('padding-bottom', '20px');
	}, function(e) {
		$(this).find('.region-actions').hide('fast');
		$(this).css('border', 'none').css('padding-bottom', '0');
	});
	
	$('.block-region .flatblock').hover(function(e) {
		$(this).find('.region-block-actions').show('fast');
		$(this).find('.editable-link').css('visibility', 'visible');
	}, function(e) {
		$(this).find('.region-block-actions').hide('fast');
		$(this).find('.editable-link').css('visibility', 'hidden');
	});
	
	$('.avail_block_list a[href=#popover]').popover({html: true});
	
});