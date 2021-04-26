def send_push(recipient, notification_to_send, context_for_notification_ser):
    # cannot use bulk send_message because we cannot set different badge value per user
    # see: https://github.com/jazzband/django-push-notifications/issues/606

    # to bypass circular import
    from apps.notification.serializers import NotificationSerializer

    most_recently_registered_device = (
        recipient.gcmdevice_set.filter(active=True).order_by("date_created").last()
    )

    # 1,2,3 번 기기에서 순서대로 로그인 한 경우, 3번에서 로그아웃했으나 2번에서 실수로 깜빡하고 로그아웃안했다고 해도
    # 2번으로 메세지를 보내면 안된다.
    if most_recently_registered_device and most_recently_registered_device.active:
        most_recently_registered_device.send_message(
            notification_to_send.plain_text,
            badge=recipient.unread_notification_count,
            extra=NotificationSerializer(
                notification_to_send,
                # request is needed at __init__
                context=context_for_notification_ser,
                fields=["target", "description"],
            ).data,
        )
