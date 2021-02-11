// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#userTable').DataTable({
      "pageLength": 5
  });
  $('#fieldTable').DataTable({
      "pageLength": 5
  });
  $('#bookedTable').DataTable({
      "pageLength": 5
  });
});
