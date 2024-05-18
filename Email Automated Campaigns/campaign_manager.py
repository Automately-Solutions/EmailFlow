class Campaign:
    def __init__(self, config_path):
        self.config_path = config_path
    
    def create_campaign(self, name, subject, from_email, template_id):
        return {"name": name, "subject": subject, "from_email": from_email, "template_id": template_id}
    
    def schedule_campaign(self, campaign, email_list):
        # Implement the logic to schedule the campaign
        pass
