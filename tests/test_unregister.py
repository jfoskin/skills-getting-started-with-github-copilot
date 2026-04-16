from urllib.parse import quote


def test_unregister_removes_participant_and_returns_success(client):
    activity_name = "Chess Club"
    email = "remove.me@mergington.edu"

    client.post(
        f"/activities/{quote(activity_name, safe='')}/signup",
        params={"email": email},
    )

    unregister_response = client.delete(
        f"/activities/{quote(activity_name, safe='')}/participants",
        params={"email": email},
    )

    assert unregister_response.status_code == 200
    assert unregister_response.json()["message"] == f"Unregistered {email} from {activity_name}"

    activities_response = client.get("/activities")
    activities = activities_response.json()

    assert email not in activities[activity_name]["participants"]
