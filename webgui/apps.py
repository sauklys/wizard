from django.apps import AppConfig
from django.core import management
from django.core.management.commands import loaddata
from threading import Thread


class WebguiConfig(AppConfig):
    name = "webgui"
    verbose_name = "APX Administration"
    kill_thread = False

    def background_cron(self):
        while not self.kill_thread:
            management.call_command("cron")
        print("Bye")

    def ready(self):
        # call cron job module
        try:
            worker = Thread(target=self.background_cron, daemon=True)
            worker.start()
        except KeyboardInterrupt:
            kill_thread = True
