# business/booking/tasks.py

import logging
from celery import shared_task
from business.booking.services.expire import expire_bookings

# Gunakan logger agar kamu bisa memantau proses di log file/console
logger = logging.getLogger(__name__)

@shared_task(name="business.booking.tasks.cleanup_expired_holds")
def cleanup_expired_holds_task():
    logger.info("Memulai proses pembersihan booking HOLD yang expired...")
    
    try:
        count = expire_bookings()
        logger.info(f"Proses selesai. {count} booking telah diubah statusnya menjadi EXPIRED.")
        return f"Success: {count} bookings expired."
    except Exception as e:
        logger.error(f"Gagal membersihkan booking: {str(e)}")
        raise e