from rest_framework import generics
from rest_framework.response import Response
from  ..Crud.base64_convertion import *
from ..models import *
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics
from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser

from ..serilizers import *


class Updateview(generics.GenericAPIView):
    serializer_class = Updateserializer
    permission_classes = [IsAuthenticated]

    parser_classes = (FormParser, MultiPartParser)

    def put(self,request,regId):
        # regId = request.data.get("regId")
        print(regId)
        try:

            d = employeeModel.objects.get(regId=regId)
            x= request.data.get('Photo')
            # bimage = get_as_base64(x)
            ser = registration_serilizer(instance=d,data=request.data)
            ser.is_valid()
            ser.save()
            return Response({
                "Status": 200,
                "Resuly": {"message": "employee updated successfully",
                           "regid": regId,
                           "success": True}
            })
        except AssertionError:
            print({"Status": 400})
            return Response({"status": 400,
                             "Reslut": {"message": "invalid body request",
                                        "sucess": False}
                             })

        except Exception as e:
            return Response({

                "status": 500,
                'Result': {"message": "employee update failed",
                           "sucess": False},
            })



class ProjectUpdate(generics.GenericAPIView):
    serializer_class = projectSerilizer
    permission_classes = [IsAuthenticated]

    parser_classes = (FormParser, MultiPartParser)

    def put(self,request):
        regId = request.data.get("regId")
        print(regId)
        try:
            print("madhu")
            d = projectModel.objects.get(regId=regId)

            # bimage = get_as_base64(x)
            ser = projectSerilizer(instance=d,data=request.data)
            ser.is_valid()
            ser.save()
            return Response({
                "Status": 200,
                "Resuly": {"message": "employee updated successfully",
                           "regid": regId,
                           "success": True}
            })
        except AssertionError:
            print({"Status": 400})
            return Response({"status": 400,
                             "Reslut": {"message": "invalid body request",
                                        "sucess": False}
                             })

        except Exception as e:
            return Response({

                "status": 500,
                'Result': {"message": "employee update failed",
                           "sucess": False},
            })



class WorkUpdate(generics.GenericAPIView):
    serializer_class = workserializer
    permission_classes = [IsAuthenticated]

    parser_classes = (FormParser, MultiPartParser)

    def put(self,request):
        regId = request.data.get("regId")
        print(regId)
        try:
            print("madhu")
            d = work_Experience.objects.get(regId=regId)

            # bimage = get_as_base64(x)
            ser = self.get_serializer(instance=d,data=request.data)
            ser.is_valid()
            ser.save()
            return Response({
                "Status": 200,
                "Resuly": {"message": "employee updated successfully",
                           "regid": regId,
                           "success": True}
            })
        except AssertionError:
            print({"Status": 400})
            return Response({"status": 400,
                             "Reslut": {"message": "invalid body request",
                                        "sucess": False}
                             })

        except Exception as e:
            return Response({

                "status": 500,
                'Result': {"message": "employee update failed",
                           "sucess": False},
            })




class qualificationupdateview(generics.GenericAPIView):
    serializer_class = qualificationserializer
    permission_classes = [IsAuthenticated]

    parser_classes = (FormParser, MultiPartParser)

    def put(self,request):
        regId = request.data.get("regId")
        print(regId)
        try:
            print("madhu")
            d = qualificationModel.objects.get(regId=regId)

            # bimage = get_as_base64(x)
            ser = self.get_serializer(instance=d,data=request.data)
            ser.is_valid()
            ser.save()
            return Response({
                "Status": 200,
                "Resuly": {"message": "employee updated successfully",
                           "regid": regId,
                           "success": True}
            })
        except AssertionError:
            print({"Status": 400})
            return Response({"status": 400,
                             "Reslut": {"message": "invalid body request",
                                        "sucess": False}
                             })

        except Exception as e:
            return Response({

                "status": 500,
                'Result': {"message": "employee update failed",
                           "sucess": False},
            })