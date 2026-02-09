require.config({
  paths: {
    vs: 'https://unpkg.com/monaco-editor@0.45.0/min/vs'
  }
});

require(['vs/editor/editor.main'], function () {

  let isUpdating = false;

  const editor = monaco.editor.create(
    document.getElementById('container'),
    {
      value: "def add(a, b):\n    return a + b",
      language: 'python',
      theme: 'vs-dark',
      automaticLayout: true
    }
  );

  editor.onDidChangeModelContent(() => {
    if (isUpdating) return;

    fetch("/translate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ code: editor.getValue() })
    })
    .then(res => res.json())
    .then(data => {
      if (!data.java_code.startsWith("//")) {
        isUpdating = true;

        const model = editor.getModel();
        model.setValue(data.java_code);

        monaco.editor.setModelLanguage(model, "java");

        isUpdating = false;
      }
    });
  });

});
