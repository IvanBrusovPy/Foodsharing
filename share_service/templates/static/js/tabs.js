let currentTab = 0;
let tabs = document.querySelectorAll('.tab');
let sign_in_form = document.getElementById("sign-up-form");
let firstname = document.getElementById("firstname");
let username = document.getElementById("username");
let password1 = document.getElementById("password1");
let password2 = document.getElementById("password2");
let city = document.getElementById("city");
let phone = document.getElementById("phone");
let address = document.getElementById("cafe_address");
let cafe_name = document.getElementById("cafe_name");
let login = document.getElementById("login");
let password = document.getElementById("password");

function showTab(n) {
	tabs[currentTab].style.display = "block";
}

function validateSignInform() {
	const loginValue = login.value.trim();
	const passwordValue = password.value.trim();
	let valid_result = true;


	if (loginValue === '') {
		setError(login, "Enter login");
		valid_result = false;
	} else {
		setSuccess(login);
	}
	if (passwordValue === '') {
		setError(password, "Enter password");
		valid_result = false;
	} else {
		setSuccess(password);
	}


	return valid_result;
}


function nextPrevTab(n) {
	if (n === 1 && validateSignUpForm() === false) {
		return 0;
	}
	if (currentTab + n !== tabs.length) {
		tabs[currentTab].style.display = "none";
		currentTab += n;
		showTab(currentTab);
		$('#sign-up-btn').html("Next").attr("type", "button");
	}
	if (currentTab + 1 === tabs.length) {
		$('#sign-up-btn').html("Submit").attr("type", "submit");

	}
}

function resetForm() {
	$('.sign-up-form').get(0).reset();
	$('.input-wrap').removeClass('error');
	$('.error').html("");
	$('.tab').css({
		"display": "none"
	});
	$('.tab').eq(0).css({
		"display": "block"
	});

	currentTab = 0;
}

$('input[type=radio][name=user_type]').change(function() {
	$('#user-city').toggle();
	$('#cafe-info').toggle();
});

$('#user-city').toggle();

$(document).ready(function() {
	$('#error').animate({
		opacity: 1,
	}, 1000, "swing");
	$('#error').animate({
		opacity: 0,
	}, 1000, 'swing');
});

const setError = (element, message) => {
	const inputControl = element.parentElement;
	const errorDisplay = inputControl.querySelector(".error");

	errorDisplay.innerHTML = message;
	inputControl.classList.add("error");
	inputControl.classList.remove("success");
	return 0
};

const setSuccess = element => {
	const inputControl = element.parentElement;
	const errorDisplay = inputControl.querySelector(".error");
	errorDisplay.innerHTML = "";
	inputControl.classList.add("success");
	inputControl.classList.remove("error");
};

function validateSignUpForm() {
	let valid_result = true;
	if (currentTab === 0) {
		const firstnameValue = firstname.value.trim();
		const usernameValue = username.value.trim();
		const password1Value = password1.value.trim();
		const password2Value = password2.value.trim();
		const passwordRegex = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{6,}$/;

		if (firstnameValue === '') {
			setError(firstname, "First name is required");
		} else if (firstnameValue.length < 4) {
			setError(firstname, "Name is less than 4 characters");
			valid_result = false;
		} else {
			setSuccess(firstname);
		}
		// alert(usernameValue);
		if (usernameValue === '') {
			setError(username, "Login name is required");
			valid_result = false;
		} else if (usernameValue.length < 4) {
			setError(username, "Login length should be more than 4 characters");
			valid_result = false;

			// } else if () {
			//     setError(username, "User with such name is already exist");
			//     valid_result = false;
		} else {
			setSuccess(username);
		}
		if (password1Value === '') {
			setError(password1, "Password is required");
			valid_result = false;
		} else if (password1Value.length < 6) {
			setError(password2, "Password length should be more than 6 characters");
			valid_result = false;
		} else if (passwordRegex.test(password1Value) === false) {
			setError(password1, "Too easy password");
			valid_result = false;
		} else {
			setSuccess(password1);
		}
		if (password1Value === "") {
			setError(password2, "Please confirm your password");
			valid_result = false;
		} else if (password1Value !== password2Value) {
			setError(password2, "Passwords does`t match");
			valid_result = false;
		} else {
			setSuccess(password2);
		}
	} else if (currentTab === 1) {
		const cityValue = city.value.trim();
		const phoneValue = phone.value.trim();
		const userTypeValue = document.querySelector("input[name=user_type]:checked").value.trim();
		const phoneRegex = /(?=.*\+[0-9]{3}\s?[0-9]{2}\s?[0-9]{3}\s?[0-9]{4,5}$)/;

		if (userTypeValue === "manager") {
			const cafe_nameValue = cafe_name.value.trim();
			const addressValue = address.value.trim();

			if (cafe_nameValue === '') {
				setError(cafe_name, "Field is required");
				valid_result = false;
			} else {
				setSuccess(cafe_name);
			}
			if (addressValue === '') {
				setError(address, "Address is required");
				valid_result = false;
			} else {
				setSuccess(address);
			}
			if (cityValue === '') {
				setError(city, "City is required");
				valid_result = false;
			} else {
				setSuccess(city);
			}
		}
		if (phoneValue === '') {
			setError(phone, "Phone required");
			valid_result = false;
		} else if (phoneRegex.test(phoneValue) === false) {
			setError(phone, "Invalid phone. Phone format: +380XX XXX XX XX");
			valid_result = false;
		} else {
			setSuccess(phone);
		}
	}
	return valid_result;
}