$(document).ready(function(){
  var code = $(".codemirror-inputarea")[0];
  var editor = CodeMirror.fromTextArea(code, {
    lineNumbers: true,
    mode: "text/x-csrc",
  });

  editor.on("change", function() {
    code.value = editor.getValue()
  })
});
