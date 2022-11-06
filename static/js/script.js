function rotate_img(id) {

    const element = document.querySelector('#photo')

    const currentRotate = parseInt(element.style.rotate) || 0

    if (id === "#btn_left") {

        element.style.rotate = `${currentRotate + 90}deg`
    } else {

        element.style.rotate = `${currentRotate - 90}deg`
    }


}