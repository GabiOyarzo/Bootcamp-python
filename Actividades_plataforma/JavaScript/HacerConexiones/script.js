var contOri = null; // Variable para guardar el contenido original
var navOri = null; // Variable para guardar el contenido original
var contenedorProvisorio = null;

function LogInOut() {
var estado = document.querySelector("#btn_login");
var contenedor = document.querySelector(".contenedor-grande");
var nav = document.querySelector(".nav");
var navTitle = document.querySelector(".nav-title");
var navLinks = document.querySelector(".nav-links");

if (estado.innerText === "LogOut") {
    contOri = contenedor.innerHTML; // Guardar el contenido original antes de eliminarlo
    navOri = nav.innerHTML; // Guardar el contenido original de los enlaces
    estado.innerText = "Login";
    contenedor.remove();
    navLinks.remove();
    estado.remove();
    navTitle.innerText = "DevConnect";
    contenedorProvisorio = document.createElement("div");
    contenedorProvisorio.classList.add("contenedor-grande");
    contenedorProvisorio.innerHTML = `
    <div class='Login'>
        <div class='encabezado'>
            <img src='https://img.freepik.com/vector-premium/desarrollo-software-programacion-codificacion-concepto-vector_123447-266.jpg' alt='photo_user' id='photo_user' class='photo'>
        </div>
        <div class='card-body'>
            <h1>¡Bienvenido a DevConnect!</h1>
            <h3>Una red social para programadores</h3>
            Encuentra recursos, resuelve desafíos y descubre las últimas tendencias tecnológicas.<br>
            Únete a nuestra comunidad y crece junto a nosotros.<br>
            ¡Gracias por unirte a DevConnect!
            <button class="btn" id="btn_login" onclick="LogInOut()">Login</button>
        </div>
    </div>`;
    document.body.appendChild(contenedorProvisorio);
    } else if (estado.innerText === "Login") {
    contenedorProvisorio.remove();
    contenedor = document.createElement("div");
    contenedor.classList.add("contenedor-grande");
    contenedor.innerHTML = contOri; // Restaurar el contenido original
    document.body.appendChild(contenedor);
    navLinks = document.createElement("ul");
    navLinks.classList.add("nav-links");
    nav.innerHTML = navOri; // Restaurar el contenido original de los enlaces
    }
}


function AcceptRequest(id) {
    var soli = document.querySelector("#n-solicitudes");
    var ami = document.querySelector("#n-amigos");
    var soliCount = parseInt(soli.innerText);
    var amiCount = parseInt(ami.innerText);
    
    if (soliCount > 0) {
        soliCount--;
        amiCount++;
        soli.innerText = soliCount;
        ami.innerText = amiCount;
        
        var card = document.getElementById(id);
        if (card) {
            card.remove();
        }
    }
}

function RejectRequest(id) {
    var soli = document.querySelector("#n-solicitudes");
    var soliCount = parseInt(soli.innerText);
    
    if (soliCount > 0) {
        soliCount--;
        soli.innerText = soliCount;
        
        var card = document.getElementById(id);
        if (card) {
            card.remove();
        }
    }
}

function EditProfile() {
    var profileName = document.querySelector('#profile-name');
    var city = document.querySelector('#city');
    var info = document.querySelector('#profile-info-1');
    
    var inputFieldName = createInputField(profileName);
    var inputFieldCity = createInputField(city);
    var inputFieldInfo = createInputField(info);
    
    inputFieldName.focus();
    
    function createInputField(element) {
        var inputField = document.createElement('input');
        inputField.type = 'text';
        inputField.value = element.innerText;
        
        inputField.addEventListener('keyup', function(event) {
            if (event.key === 'Enter') {
                element.innerText = inputField.value;
                inputField.parentNode.removeChild(inputField);
            }
        });
        
        element.parentNode.insertBefore(inputField, element.nextSibling);
        
        return inputField;
    }
}
