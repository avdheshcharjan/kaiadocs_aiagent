# Setting Up Your Environment Variables

## Creating the .env File

1. Navigate to your project directory:
```bash
cd generative-ai-docs
```

2. Create a new `.env` file:
```bash
touch .env
```

3. Open the `.env` file in your preferred text editor and add the following line:
```bash
export GOOGLE_API_KEY=<your-api-key>
```

## Important Notes

- Replace `<your-api-key>` with your actual Google API key
- Do not include any quotes or spaces around the API key
- Make sure the `.env` file is in the root of your `generative-ai-docs` directory
- Keep your API key secure and never commit it to version control

## Using the .env File

1. To load the environment variables, source the file:
```bash
source .env
```

2. Verify the environment variable is set:
```bash
echo $GOOGLE_API_KEY
```

## Security Best Practices

- Add `.env` to your `.gitignore` file to prevent accidentally committing sensitive information
- Keep a template file (e.g., `.env.example`) in version control with dummy values
- Regularly rotate your API keys
- Never share your API key in public repositories or discussions

## Troubleshooting

If the environment variable isn't being recognized:
- Ensure you've sourced the `.env` file
- Check for any typos in the variable name
- Verify the file permissions are correct
- Make sure there are no hidden characters in the `.env` file

For more information about securing API keys, refer to Google's official documentation.
