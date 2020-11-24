# calAPI

calAPI is a simple and intuitive API for generating and downloading .ics files with WEEIA events. 


## Usage

The only endpoint of the API is:

/calAPI/year=`<year>`/month=`<month>`

,where `<year>` and `<month>` should be replaced with desired year and month, respectively.

## Usage examples 

/calAPI/year=2020/month=10
download for calAPI.ics starts

/calAPI/year=2020/month=3
download for calAPI.ics starts

/calAPI/year=a/month=b
Error: values are wrong

/calAPI/year=a/month=b
Error: values are wrong

Generated files can be viewed in "examples" folder.
