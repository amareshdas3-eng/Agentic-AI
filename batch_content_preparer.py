import os
import json
import datetime
from cloud_post_scheduler import TOPICS_DATABASE

BATCH_DIR = "d:/instagram/batch_queue_30days"
os.makedirs(BATCH_DIR, exist_ok=True)

def generate_30day_schedule():
    """
    Builds a structured 30-day publishing calendar with 2-3 posts per day.
    Saves metadata, captions, media specifications, and optimal posting times.
    """
    start_date = datetime.date.today()
    schedule = []
    
    slots_config = [
        {"slot": "morning", "time": "09:30:00", "pillar": "Forensic Teardown"},
        {"slot": "afternoon", "time": "14:30:00", "pillar": "Technical Carousel"},
        {"slot": "evening", "time": "20:30:00", "pillar": "Industrial AI & Dialogue"}
    ]
    
    total_posts = 0
    for day_offset in range(30):
        current_date = start_date + datetime.timedelta(days=day_offset)
        date_str = current_date.strftime("%Y-%m-%d")
        day_name = current_date.strftime("%A")
        
        for slot_info in slots_config:
            slot_name = slot_info["slot"]
            topics = TOPICS_DATABASE[slot_name]
            topic = topics[day_offset % len(topics)]
            
            total_posts += 1
            scheduled_datetime = f"{date_str}T{slot_info['time']}+05:30"
            
            post_entry = {
                "post_number": total_posts,
                "date": date_str,
                "day": day_name,
                "slot": slot_name,
                "pillar": slot_info["pillar"],
                "scheduled_publish_time_ist": scheduled_datetime,
                "title": topic["title"],
                "format": topic["format"],
                "keyword_trigger": topic["keyword"],
                "suggested_caption": (
                    f"⚡ {topic['title']} ⚡\n\n"
                    f"{topic['hook']}\n\n"
                    f"👇 Comment '{topic['keyword']}' below to get the full technical protocol! #ProEngineering #PowerSystems #Substation"
                )
            }
            schedule.append(post_entry)
            
    queue_file = os.path.join(BATCH_DIR, "30day_cloud_queue_schedule.json")
    with open(queue_file, "w", encoding="utf-8") as f:
        json.dump(schedule, f, indent=2)
        
    print(f"Generated 30-Day Batch Schedule ({len(schedule)} total posts) at: {queue_file}")
    return schedule

if __name__ == "__main__":
    generate_30day_schedule()

