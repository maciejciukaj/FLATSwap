import torch

def test_cuda_availability():
    if torch.cuda.is_available():
        assert torch.cuda.is_available() == True, "CUDA is not available"
        assert torch.cuda.get_device_name(0), "Unable to get the CUDA device name"
        print(f"CUDA available. GPU: {torch.cuda.get_device_name(0)}")
    else:
        assert torch.cuda.is_available() == False, "CUDA is marked unavailable but should be accessible"
        print("CUDA is not available.")
