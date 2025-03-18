document.addEventListener("DOMContentLoaded", function () {
  const followBtn = document.getElementById("follow-btn");
  const followersCount = document.getElementById("followers-count");

  if (followBtn) {
    followBtn.addEventListener("click", function () {
      const profileId = this.dataset.profileId;
      const csrfToken = this.dataset.csrf;

      fetch(`/profile/follow/${profileId}/`, {
        method: "POST",
        headers: {
          "X-CSRFToken": csrfToken,
          "Content-Type": "application/json",
        },
        credentials: "same-origin",
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.status === "success") {
            // Update button text and class
            if (data.is_following) {
              followBtn.textContent = "Unfollow";
              followBtn.classList.add("following");
            } else {
              followBtn.textContent = "Follow";
              followBtn.classList.remove("following");
            }

            // Update followers count
            followersCount.textContent = `Followers: ${data.followers_count}`;
          } else {
            console.error(data.message);
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    });
  }
});

document.querySelector(".open-sidebar").addEventListener("click", function () {
  document.querySelector(".sidebar").classList.toggle("open");
});

document.querySelector(".close-sidebar").addEventListener("click", function () {
  document.querySelector(".sidebar").classList.toggle("open");
});
