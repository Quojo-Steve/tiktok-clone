const menu = document.querySelector(".menu")
const dropDown = document.querySelector(".drop-down")
const searchBtn = document.querySelector(".small")
const closeBtn = document.querySelector(".close")
const searchBar = document.querySelector(".search-bar")
const smallSearch = document.querySelector(".small-search")


searchBtn.addEventListener("click", () => {
    smallSearch.style.display = "block"
    searchBtn.style.display = "none"
    closeBtn.style.display = "block"
    console.log("Hello")
});

closeBtn.addEventListener("click", () => {
    smallSearch.style.display = "none"
    searchBtn.style.display = "block"
    closeBtn.style.display = "none"
    console.log("Hello")
});

dropDown.addEventListener("mouseenter", () => {
    menu.classList.remove("hidden")
})

menu.addEventListener("mouseleave", () => {
    menu.classList.add("hidden")
})

let video = document.querySelectorAll("video")
video.forEach(video => {
    let playPromise = video.play()
    if(playPromise !== undefined) {
        playPromise.then(() => {
            let observer = new IntersectionObserver(entries => {
                entries.forEach(entry => {
                    video.muted = false
                    if(entry.intersectionRatio !== 1 && !video.paused){
                        video.pause()
                    } else if (entry.intersectionRatio > 0.5 && video.paused) {
                        video.play()
                    }
                })
            }, {threshold: 0.5})
            observer.observe(video)
        })
    }
})
