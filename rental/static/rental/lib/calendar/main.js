document.addEventListener("DOMContentLoaded", () => {
    const calendarEl = document.getElementById("calendar");
    const calendar = new FullCalendar.Calendar(calendarEl, {
      headerToolbar: {
        left: "prev,next",
        right: "title",
      },
      locale: "fr",
      firstDay: 1, // week start on Monday
      displayEventTime: false, // don't show the time column in list view
      googleCalendarApiKey: "AIzaSyC2Wcg2Q2sq071w_L6k5JfHnPptlseU16g",
      events: {
        googleCalendarId:
          "burik7aclvhc7vsboh06c179uo@group.calendar.google.com",
      },
      // eventColor: "#378006",
      contentHeight: "auto",
      // don't navigate in main tab
      eventClick: (arg) => {
        arg.jsEvent.preventDefault();
      },
      themeSystem: "bootstrap",

      loading: (bool) => {
        document.getElementById("loading").style.display = bool
          ? "block"
          : "none";
      },
    });

    calendar.render();
  });