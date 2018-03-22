$(document).ready(function(){
  var code = $(".codemirror-textarea")[0];
  var editor = CodeMirror.fromTextArea(code, {
    lineNumbers: true,
    mode: "text/x-csrc",
    readOnly: true
  });
  editor.setSize(null, 100);

  code = $(".codemirror-textarea")[1];
  var editor = CodeMirror.fromTextArea(code, {
    lineNumbers: true,
    mode: "text/x-csrc",
    readOnly: true
  });
  editor.setSize(null, 100);

  code = $(".codemirror-textarea")[2];
  var editor = CodeMirror.fromTextArea(code, {
    lineNumbers: true,
    mode: "text/x-csrc",
    readOnly: true
  });
  editor.setSize(null, 140);

  code = $(".codemirror-textarea")[3];
  var editor = CodeMirror.fromTextArea(code, {
    lineNumbers: true,
    mode: "text/x-csrc",
    readOnly: true
  });
  editor.setSize(null, 160);

});
