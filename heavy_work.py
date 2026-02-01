from datetime import datetime, timezone
import time


def now():
    return datetime.now(timezone.utc).isoformat()


def do_heavy_work(request_id: str):
    print(f"[{now()}] START heavy_work request_id={request_id}")

    # symulacja ciężkiej pracy
    time.sleep(2)

    print(f"[{now()}] END heavy_work request_id={request_id}")

    return {
        "processed_at": now(),
        "request_id": request_id
    }