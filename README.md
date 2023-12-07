# Spotify Direct Links in Discord

[![invite-badge][]][invite]

A small bot that provides native links using the `spotify` protocol.

Here is an example:

![example-image]

[invite]: https://discord.com/oauth2/authorize?client_id=813784061092036608&permissions=18432&scope=bot
[invite-badge]: https://img.shields.io/badge/Invite%20the%20bot-Click%20here-7289DA?style=for-the-badge&logo=spotify
[example-image]: https://github.com/NicoKandut/discord-native-spotify-links/blob/main/example.png?raw=true



AWS SNS Integration:

A new AWS SNS topic ARN (SNS_TOPIC_ARN) is specified in the code.
The boto3 library is used to create an SNS client (sns_client) with the specified AWS region.

Publishing to SNS:

When a Spotify link is detected, the direct link is sent as a message to the Discord channel.
Simultaneously, the direct link is published to the AWS SNS topic using sns_client.publish().
Test Case:

In the test case, after simulating a user sending a Spotify link, the test asserts that the direct_link variable holds the expected direct link.
This ensures that the Discord bot is generating the direct link correctly and publishing it to AWS SNS.
AWS Credentials:

Ensure that your AWS credentials (access key and secret key) are properly configured, either through environment variables, AWS CLI configuration, or an IAM role if running on an AWS resource.
Before running the code, make sure to replace placeholders such as 'your-aws-region' and 'your-sns-topic-arn' with your actual AWS region and SNS topic ARN.

Additionally, you should have the necessary AWS SDK (boto3) installed. You can install it using:


pip install boto3

Please adjust the code according to your specific use case and AWS setup.

Efficient Navigation:

Deeplinks provide a direct and efficient way to navigate to specific pages or functionalities within an application. In the context of test automation, this efficiency contributes to faster and more targeted test execution

Usage of AWS SNS Topics enables the distribution of test results, events, or notifications to relevant stakeholders or systems.
