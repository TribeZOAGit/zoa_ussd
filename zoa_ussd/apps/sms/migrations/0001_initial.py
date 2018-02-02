# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-02 05:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SMSGateway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=20)),
                ('service_provider', models.IntegerField(choices=[(1, "Africa's Talking")], null=True)),
                ('api_key', models.CharField(help_text="For Africas' Talking, this is the username", max_length=100)),
                ('api_secret', models.CharField(help_text="For Africas' Talking, this is the api key", max_length=100)),
                ('is_sandbox', models.NullBooleanField()),
                ('short_code', models.CharField(blank=True, max_length=20, null=True)),
                ('sender_id', models.CharField(blank=True, max_length=20, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SMSMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_type', models.IntegerField(choices=[(1, 'SMS IN'), (2, 'SMS OUT')])),
                ('message', models.CharField(max_length=480)),
                ('sender_id', models.CharField(max_length=50)),
                ('message_id', models.CharField(max_length=50, null=True)),
                ('recipient_id', models.CharField(max_length=50)),
                ('cost', models.CharField(max_length=30, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Success'), (2, 'Error')], null=True)),
                ('at_delivery_status', models.CharField(choices=[('Sent', 'The message has successfully been sent by our network.'), ('Submitted', 'The message has successfully been submitted to the MSP (Mobile Service Provider).'), ('Buffered', 'The message has been queued by the MSP.'), ('Rejected', 'The message has been rejected by the MSP. This is a final status.'), ('Success', "The message has successfully been delivered to the receiver's handset. This is a final status."), ('Failed', "The message could not be delivered to the receiver's handset. This is a final status.")], max_length=9, null=True)),
                ('at_delivery_failure_reason', models.CharField(choices=[('InsufficientCredit', "This occurs when the subscriber don't have enough airtime for a premium subscription service/message"), ('InvalidLinkId', 'This occurs when a message is sent with an invalid linkId for an onDemand service'), ('UserIsInactive', 'This occurs when the subscriber is inactive or the account deactivated by the MSP (Mobile Service Provider).'), ('UserInBlackList', 'This would occur if the user has been blacklisted not to receive messages from a paricular service (shortcode or keyword)'), ('UserAccountSuspended', 'This would occur when the mobile subscriber has been suspended by the MSP.'), ('NotNetworkSubcriber', "This occurs when the message is passed to an MSP where the subscriber doesn't belong."), ('UserNotSubscribedToProduct', 'This is for a subscription product which the subscriber has not subscribed to.'), ('UserDoesNotExist', 'This occurs when the message is sent to a non-existent mobile number.'), ('DeliveryFailure', "This occurs when message delivery fails for any reason not listed above or where the MSP didn't provide a delivery failure reason.")], max_length=26, null=True)),
                ('delivered', models.NullBooleanField()),
                ('time_delivered', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sms_gateway', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.SMSGateway')),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=20)),
                ('template_text', models.CharField(max_length=400)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='smsmessage',
            name='template',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sms.Template'),
        ),
    ]