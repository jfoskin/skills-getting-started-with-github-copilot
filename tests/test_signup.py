from urllib.parse import quote


def test_signup_adds_participant_and_returns_success(client):
    activity_name = "Chess Club"
    email = "new.student@mergington.edu"

    signup_response = client.post(
        f"/activities/{quote(activity_name, safe='')}/signup",
        params={"email": email},
    )

    assert signup_response.status_code == 200
    assert signup_response.json()["message"] == f"Signed up {email} for {activity_name}"

    activities_response = client.get("/activities")
    activities = activities_response.json()

    assert email in activities[activity_name]["participants"]
