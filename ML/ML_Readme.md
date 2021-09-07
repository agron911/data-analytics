## All the code is reference from Hands-On Unsupervised Learning Using Python book
I'm trying to translate it into English while I'm studying it, It'll be much more easier for me to
review if I had to.

### Issues
You might wondering where can you get the datasets that we apply in the code
First you have to install AWS client which is Amazon's cloud server,
```
pip install awscli==1.19.28
```
Later on, you can download the datasets from the cloud using aws s3
```
aws s3 cp s3://handson-unsupervised-learning/datasets/ datasets --recursive --no-sign-request

```
