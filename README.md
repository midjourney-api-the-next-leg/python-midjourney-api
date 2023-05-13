# The Next Leg

The Next Leg is a module that provides functionality for creating AI-generated images with Midjourney. It provides a simple interface for interacting with Midjourney's API and performing various actions such as creating images from prompts or URLs, describing images, using buttons or slash commands, and getting/setting account settings.

## Installation

To use this package, you need to have Python installed on your machine. You can install TNL using pip:

```sh
pip install midjourney-api
```

## Usage

Here is an example of how to use the TNL package to create an image from a prompt:

```
from tnl import TNL

TNL_API_KEY = 'your_api_key_here'
tnl = TNL(TNL_API_KEY)

prompt = 'a cat playing the piano'
response = tnl.imagine(prompt)

print(response)
```

## API

### `TNL(api_key: str)

Creates a new instance of `TNL` with the provided `apiKey`.

### Imagine

`tnl.imagine(prompt: str, ref: str = '', webhook_override: str = '')`

Creates a new image from a prompt.

- `prompt` - The prompt you want to use to generate the image.
- `ref` (optional) - A reference string that will be returned in the webhook response.
- `webhook_override` (optional) - A webhook URL that will be used instead of the one set in the dashboard.

### Get Progress and Message Result

`tnl.get_message_and_progress(message_id: str, expire_mins: Optional[int] = None)`

Gets the progress and response of a message.

- `message_id` - The message ID of the message you want to get the progress and response for.
- `expire_mins` (optional) - A timeout for the request in minutes. If the request takes longer than this, it will return as 'incomplete'

### Img 2 Img

`tnl.img2img(prompt: str, img_url: str, ref: str = '', webhook_override: str = '')`

Creates an image from a prompt and an image.

- `prompt` - The prompt you want to use to generate the image.
- `img_url` - The URL of the image you want to use as the base image.
- `ref` (optional) - A reference string that will be returned in the webhook response.
- `webhook_override` (optional) - A webhook URL that will be used instead of the one set in the dashboard.

### Describe

`tnl.describe(img_url: str, ref: str = '', webhook_override: str = '')`

Describes an image.

- `img_url` - The URL of the image you want to describe.
- `ref` (optional) - A reference string that will be returned in the webhook response.
- `webhook_override` (optional) - A webhook URL that will be used instead of the one set in the dashboard.

### Button

`tnl.button(button: TNLTypes.ButtonTypes, button_message_id: str, ref: str = '', webhook_override: str = '')`

Uses a button on an image.

- `button` - A button type.
- `button_message_id` - The button_message_id of the message that contains the button.
- `ref` (optional) - A reference string that will be returned in the webhook response.
- `webhook_override` (optional) - A webhook URL that will be used instead of the one set in the dashboard.

### Get Seed

`tnl.getSeed(message_id: string): Promise<TNLTypes.Response.Seed>`

Gets a seed of a message.

- `message_id` - The message ID of the message you want to get the seed for.

### Slash Command

`tnl.slashCommand(slashCommand: TNLTypes.SlashCommands, ref?: string, webhook_override?: string)`

Uses a slash command such as relax, fast, private, or stealth.

- `slashCommand` - A slash command type.
- `ref` (optional) - A reference string that will be returned in the webhook response.
- `webhook_override` (optional) - A webhook URL that will be used instead of the one set in the dashboard.

### Get Settings

`tnl.getSettings(): Promise<TNLTypes.Response.Message>`

Gets the settings available for your account.

### Set Settings

`tnl.setSettings(settings: TNLTypes.Settings, ref?: string, webhook_override?: string)`

Sets the settings for your account.

- `settings` - The settings you want to set.
- `ref` (optional) - A reference string that will be returned in the webhook response.
- `webhook_override` (optional) - A webhook URL that will be used instead of the one set in the dashboard.

### Get Info

`tnl.getInfo(ref?: string, webhook_override?: string)`

Gets information about your account including Fast Time Remaining, Job Mode, Queued Jobs and more.

- `ref` (optional) - A reference string that will be returned in the webhook response.
- `webhook_override` (optional) - A webhook URL that will be used instead of the one set in the dashboard.

### Get Seed

`tnl.getSeed(message_id: str)`

Gets a seed of a message.

- `message_id` - The message ID of the message you want to get the seed for.

### Slash Command

`tnl.slashCommand(slash_command: TNLTypes.SlashCommands, ref: str = '', webhook_override: str = '')`

Uses a slash command such as relax, fast, private, or stealth.

- `slash_command` - A slash command type.
- `ref` (optional) - A reference string that will be returned in the webhook response.
- `webhook_override` (optional) - A webhook URL that will be used instead of the one set in the dashboard.

### Get Settings

`tnl.getSettings()`

Gets the settings available for your account.

### Set Settings

`tnl.setSettings(settings: TNLTypes.Settings, ref: str = '', webhook_override: str = '')`

Sets the settings for your account.

- `settings` - The settings you want to set.
- `ref` (optional) - A reference string that will be returned in the webhook response.
- `webhook_override` (optional) - A webhook URL that will be used instead of the one set in the dashboard.

### Get Info

`tnl.getInfo(ref: str = '', webhook_override: str = '')`

Gets information about your account including Fast Time Remaining, Job Mode, Queued Jobs and more.

- `ref` (optional) - A reference string that will be returned in the webhook response.
- `webhook_override` (optional) - A webhook URL that will be used instead of the one set in the dashboard.
