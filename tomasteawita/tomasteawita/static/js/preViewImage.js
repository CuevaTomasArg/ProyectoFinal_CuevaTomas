const $id_image = document.querySelector("#id_image"),
  $imagePreView = document.querySelector("#imagePreView");

// document.getElementById('id_description').remove()

// var formBody = document.getElementById("formBody")

// var texatArea = document.createElement("textarea")
// texatArea.setAttribute('id','id_description')
// texatArea.setAttribute('value','Escribe la descripcion del post')
// texatArea.setAttribute('name','description')
// texatArea.setAttribute('type','text')
// texatArea.setAttribute('maxlength','1024')

// formBody.children[1].appendChild(texatArea)



$id_image.addEventListener("change", () => {
  const field = $id_image.files;
  if (!field || !field.length) {
    $imagePreView.src = "";
    return;
  }
  
  const firstField = field[0];
  const objectURL = URL.createObjectURL(firstField);
  $imagePreView.src = objectURL;
});